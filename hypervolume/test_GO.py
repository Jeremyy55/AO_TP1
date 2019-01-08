from GO import compute_hypervolum_surface


def test_compute_hypervolum_surface_3d():
    assert compute_hypervolum_surface([[3,10,10],[6,5,10],[10,2,10],[4,10,7],[6,7,7],[10,7,4],[10,10,3]],[10,10,10],[[3,5,7],[6,2,4],[4,7,3],[10,0,0],[0,10,0],[0,0,10]])== 273

def test_compute_hypervolum_surface_2d():
    assert compute_hypervolum_surface([[2,5],[3,4],[5,3],[7,2]],[7,5],[[7,0],[0,5],[3,3],[2,4],[5,2]])==11   