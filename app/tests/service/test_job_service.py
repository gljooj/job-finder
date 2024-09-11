import unittest

from app.service.job_service import JobService


class TestJobService(unittest.TestCase):
    def setUp(self):
        self.service = JobService()

    def test_create_job_success(self):
        job_data = {
            "category": "Landscaping",
            "location": "Glades FL"
        }
        result = self.service.create_job(job_data)
        self.assertEqual(result.category, "Landscaping")

    def test_create_job_failed(self):
        try:
            job_data = {
            }
            self.service.create_job(job_data)
        except Exception as e:
            assert 'location must be on payload.' in e.args

    def test_create_job_missing_data(self):
        with self.assertRaises(ValueError):
            job_data = {
                "category": "Landscaping"
            }
            self.service.create_job(job_data)

    def test_find_job_by_id_success(self):
        job_id = 1
        result = self.service.find_job_by_id(job_id)
        self.assertEqual(result["id"], job_id)

    def test_find_job_by_id_failure(self):
        with self.assertRaises(ValueError):
            self.service.find_job_by_id(999)

    def test_get_jobs(self):
        result = self.service.get_jobs()
        assert result is not None

