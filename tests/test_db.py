from uuid import uuid4

import pytest
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import CRUD
from db import get_db

"""
Tests to verify the CRUD base class raises not implemented errors
"""


class TestCrud:
    def test_create(self, db: Session = Depends(get_db)):
        with pytest.raises(NotImplementedError):
            CRUD.create(db, "")

    def test_update(self, db: Session = Depends(get_db)):
        with pytest.raises(NotImplementedError):
            CRUD.update(db, uuid4(), "", "")

    def test_read_by_id(self, db: Session = Depends(get_db)):
        with pytest.raises(NotImplementedError):
            CRUD.read_by_id(db, uuid4())

    def test_delete_by_id(self, db: Session = Depends(get_db)):
        with pytest.raises(NotImplementedError):
            CRUD.delete_by_id(db, uuid4())
