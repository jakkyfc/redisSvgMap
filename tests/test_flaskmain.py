import unittest
import os
import io
import json
import sys
from unittest import mock
from flaskmain import app

class TestOfFlaskApps(unittest.TestCase):
  def setUp(self):
    self.main = app.test_client();

  def test_access2RootPath(self):
    response = self.main.get("/")
    self.assertEqual(response.status_code, 200)
    
  def test_access2QueryPath(self):
    response = self.main.get("/query?hello=b")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data.decode("UTF-8"), "QUERY:hello=b : b")
  
  def test_access2rtDatasetPath(self):
    response = self.main.get("/dataset/show")
    self.assertEqual(response.status_code, 200)

  def test_access2IndexFile(self):
    response = self.main.get("/svgmap/index.html")
    self.assertEqual(response.status_code, 200)
    response.close()