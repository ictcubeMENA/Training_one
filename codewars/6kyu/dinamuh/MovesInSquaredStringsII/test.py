from main import oper
from main import rot
from main import selfie_and_rot


def test_oper(benchmark):
    assert benchmark(oper, rot,
                     "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL") == "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif"
    assert benchmark(oper, rot, "rkKv\ncofM\nzXkh\nflCB") == "BClf\nhkXz\nMfoc\nvKkr"
    assert benchmark(oper, selfie_and_rot,
                     "xZBV\njsbS\nJcpN\nfVnP") == "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx"
    assert benchmark(oper, selfie_and_rot,
                     "uLcq\nJkuL\nYirX\nnwMB") == "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu"
