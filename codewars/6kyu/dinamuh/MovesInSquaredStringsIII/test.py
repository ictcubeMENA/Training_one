import unittest
from main import oper
from main import diag_1_sym
from main import rot_90_clock
from main import selfie_and_diag1




def test_oper(benchmark):
    assert benchmark(oper,rot_90_clock, "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb")=="Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle"
    assert benchmark(oper,diag_1_sym, "wuUyPC\neNHWxw\nehifmi\ntBTlFI\nvWNpdv\nIFkGjZ")=="weetvI\nuNhBWF\nUHiTNk\nyWflpG\nPxmFdj\nCwiIvZ"
    assert benchmark(oper,selfie_and_diag1, "NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg")=="NJVGhr|NMtsrz\nMObsvw|JOPotj\ntPhCtl|VbhEQl\nsoEnhi|GsCnRi\nrtQRLK|hvthLW\nzjliWg|rwliKg"

