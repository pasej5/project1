# import asyncio

# # Asynchronous generator function
# async def async_generator():
#     for i in range(5):
#         yield i
#         if i == 2:
#             # Introduce a sleep of 1 second after yielding the value 2
#             await asyncio.sleep(5)

# # Using set comprehension with asynchronous generator
# async def main():
#     agen = async_generator()

#     # Create a task for the asynchronous generator
#     task = asyncio.create_task(async_set_comprehension(agen))

#     # Do other tasks or operations here

#     # Wait for the completion of the task
#     await task

# # Asynchronous set comprehension with sleep
# async def async_set_comprehension(agen):
#     result_set = {i async for i in agen}
#     print(result_set)

# # Run the event loop
# asyncio.run(main())



