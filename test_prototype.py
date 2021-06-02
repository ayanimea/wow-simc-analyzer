import pytest
from prototype import Report

def test_read_report():
    vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
    report = Report()
    title = report.read_report(vgm_url)
    assert (title == '<title>VGMusic.com - Nintendo Music</title>') 
