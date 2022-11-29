import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config


MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, tls=True, tlsAllowInvalidCertificates=True)


database = client.customers


customer_collection = database.get_collection("students_collection")

# helpers

def customer_helper(customer) -> dict:
    return {
        "id": str(customer["_id"]),
        "username": customer["username"],
        "full_name": customer["full_name"],
        "email": customer["email"],
        "year": customer["year"],
    }


# crud operations


# Retrieve all students present in the database
async def retrieve_customers():
    customers = []
    async for customer in customer_collection.find():
        customers.append(customer_helper(customer))
    return customers


# Add a new student into to the database
async def add_customer(customer_data: dict) -> dict:
    customer= await customer_collection.insert_one(customer_data)
    new_customer = await customer_collection.find_one({"_id": customer.inserted_id})
    return customer_helper(new_customer)


# Retrieve a student with a matching ID
async def retrieve_customer(id: str) -> dict:
    customer = await customer_collection.find_one({"_id": ObjectId(id)})
    if customer:
        return customer_helper(customer)


# Update a student with a matching ID
async def update_customer(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    customer = await customer_collection.find_one({"_id": ObjectId(id)})
    if customer:
        updated_customer = await customer_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_customer:
            return True
        return False


# Delete a student from the database
async def delete_customer(id: str):
    student = await customer_collection.find_one({"_id": ObjectId(id)})
    if student:
        await customer_collection.delete_one({"_id": ObjectId(id)})
        return True

