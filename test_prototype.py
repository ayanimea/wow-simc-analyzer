import pytest
import tempfile
import os
from prototype import Report

def test_read_report():
    test_url = 'http://perdu.com'
    report = Report(test_url)
    title = report.read_report()
    assert (title == 'b\'<title>Vous Etes Perdu ?</title>\'') 

def test_convert_report_to_xls():
    test_url = 'http://perdu.com'
    dirpath = tempfile.mkdtemp(prefix='simc-analyzer-')
    path = os.path.join(dirpath, 'test.xls')
    try:
        assert(not os.path.exists(path))
        report = Report(test_url)
        report.convert_report_to_xls(path)
        assert(os.path.exists(path))
    finally:
        if os.path.exists(path):
            os.remove(path)
