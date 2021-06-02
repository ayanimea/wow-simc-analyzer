import pytest
from prototype import Report

def test_read_report():
    vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
    report = Report(vgm_url)
    title = report.read_report()
    assert (title == '<title>VGMusic.com - Nintendo Music</title>') 
