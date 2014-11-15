import numpy as np


def dti_design_matrix(bvecs, bvals)

    """  
    Construct a design 
    For each measured direction, v = bvec*bval, at each voxel, there is a
    tensor, Q, such that v'Qv = data.  Data is the diffusion signal, 

    data = S0 exp(-b v'Qv).  

    Consequently,  

    ln(data/S0) = (-b) * (v'Qv), or
    ln(data)  = ln(S0) + (-b) * (v'Qv)  

    Call ln(data) = d. The measurement directions are the same at every
    voxel. Hence, we expand (v'Qv) into a quadratic equation for each voxel,

    d = ln(S0) +  -b * (v1v1 q11 + v2v2 q22 + ... 2 v2 v3 q23 + ... )
    d = ln(S0) +   V * q, 

    where V is a nDirections by 6 matrix and d are the data in all the
    directions. The solution, q, is the tensor (quadratic form) for that
    voxel.

    Start with q, which will have a row for each volume, each row having
    three elements: [bvx bvy bvz].

    Each row of X corresponds to a DW direction for that volume of the form:
    [-b bvx bvx, -b bvy bvy, -b bvz bvz, -2b bvx bvy, -2b bvx bvz, -2b bvy bvz].

    The six values in each row of X: [-bx^2 -by^2 -bz^2 -2bxy -2bxz
    -2byz] are the six unique values in the symmetric b-matrix. These are
    the same as equation 1 on p.457 of Basser et al, 2002, NMR in
    Biomedicine.
    """ 
    q = bvecs.T * sqrt(repmat(bvals, 1, 3)));
    X = [-q[:,1]*2 -q(:,2)**2 -q(:,3)**2 -2.*q(:,1).*q(:,2) -2.*q(:,1).*q(:,3) -2.*q(:,2).*q(:,3)];

    return X


