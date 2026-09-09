from job_processing_engine.job import Job
from job_processing_engine.customer import Customer

def test_job_object_creation():
    # create customer object
    customer = Customer(1, "Joseph", "jl2@gmail.com", is_active=False)
    job = Job(100, customer=customer)
    assert job.id == 100
    assert job.attempts == 0
    assert job.result is None
    assert job.status == "pending"
    assert job.customer.name == "Joseph"


def test_job_starts():
    customer = Customer(111, "Mark", "Mark_stain@gmail.com", is_active=True)
    job = Job(111, customer)
    assert job.status == "pending"
    assert job.attempts == 0
    job.start()
    assert job.status == "running"
    assert job.attempts == 1

def test_job_doesnot_starts_run_twice():
    customer = Customer(111, "Mark", "Mark_stain@gmail.com", is_active=True)
    job = Job(111, customer)
    assert job.status == "pending"
    assert job.attempts == 0
    # start job once
    job_status_1 = job.start()
    assert job_status_1 is True
    assert job.status == "running"
    assert job.attempts == 1
    # start job again
    job_status_2 = job.start()
    assert job_status_2 is False
    assert job.status == "running"
    assert job.attempts == 1