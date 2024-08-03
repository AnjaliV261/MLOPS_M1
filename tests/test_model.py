import unittest
from src.model import train_model
import os

class TestModel(unittest.TestCase):
    def test_model_training(self):
        # Train the model
        train_model()
        
        # Check if the model file is created
        self.assertTrue(os.path.exists('model.joblib'))

if __name__ == "__main__":
    unittest.main()
