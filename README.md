# RubiscapeAssignment
Task- Event Scheduler
Tech stack- python, Django, celery, redis, Pytest for Unit testing
Process-
1. Create Django model, take input event details from user if date is previous then it will not save data to database,
2. Performed CRUD operations on database
3. When user enter evnet details after saving data to database, using celery  it will schedule email reminder to user
4. Performed Unit tesing using Pytest.   
