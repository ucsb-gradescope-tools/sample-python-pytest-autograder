import pytest
import pytest_utils
from pytest_utils.decorators import max_score, visibility, tags

from labxx import *

@max_score(10)
def test_addEm_1():
  assert addEm(2,4)==6

@max_score(20)
@visibility('after_due_date')
def test_addEm_2():
    assert addEm(3,1)==4

@max_score(20)
@visibility('hidden')
def test_addEm_3():
  assert addEm(3,1)==4
    
