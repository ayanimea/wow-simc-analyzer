import pytest
import tempfile
import os
from prototype import Report

def test_read_report():
    test_url = 'http://perdu.com'
    report = Report(test_url)
    raw_report = report.read_report()
    assert (raw_report.head.encode("utf-8") == b'<head><title>Vous Etes Perdu ?</title></head>')
    assert (raw_report.title.encode("utf-8") == b'<title>Vous Etes Perdu ?</title>') 
    assert (raw_report.body.encode("utf-8") == b"<body><h1>Perdu sur l'Internet ?</h1><h2>Pas de panique, on va vous aider</h2><strong><pre>    * &lt;----- vous \xc3\xaates ici</pre></strong></body>") 

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
