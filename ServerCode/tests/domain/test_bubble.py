"""
Test Scantron model.
"""

import uuid
from bubbleScan.domain.scantron import Scantron

def test_scantron_model_init():
	"""
	Test Scantron model initialization.
	"""
	code = uuid.uuid4()
	first = "John"
	last = "Charlie"
	idNumber = 34563

	scantron = Scantron(code, first, last, idNumber)

	assert scantron.code == code
	assert scantron.first == "John"
	assert scantron.last == "Charlie"
	assert scantron.idNumber == 34563

def test_scantron_model_from_dict():
	"""
	Test creating Scantron model from dictionary.
	"""
	code = uuid.uuid4()
	init_dict = {"code": code, "first": "John", "last": "Charlie", "idNumber": 34563 }

	scantron = Scantron.from_dict(init_dict)

	assert scantron.code == code
	assert scantron.first == "John"
	assert scantron.last == "Charlie"
	assert scantron.idNumber == 34563

def test_scantron_model_to_dict():
	"""
	Test converting Scantron model to dictionary.
	"""

	init_dict = {"code": uuid.uuid4(), "first": "John", "last": "Charlie", "idNumber": 34563 }

	scantron = Scantron.from_dict(init_dict)

	assert scantron.to_dict() == init_dict

def test_scantron_model_comparison():
	"""
	Test equality comparison of Scantron models.
	"""

	init_dict = {"code": uuid.uuid4(), "first": "John", "last": "Charlie", "idNumber": 34563 }

	scantron1 = Scantron.from_dict(init_dict)
	scantron2 = Scantron.from_dict(init_dict)

	assert scantron1 == scantron2
