import numpy as np
import numpy.testing as npt

# bvecs are taken from the camino electro-points:
bvecs = np.array([[0.5578, 0.7900, 0.2545],
                  [0.5699, -0.2588, -0.7799],
                  [-0.1955, -0.8807, 0.4314],
                  [0.9322   -0.3495   -0.0940],
                  [0.5495   -0.6605    0.5116],
                  [-0.0150   -0.2970    0.9548],
                  [0.8186    0.0957    0.5664],
                  [-0.8336   -0.3927    0.3884],
                  [0.1752    0.4790    0.8602],
                  [-0.2997    0.9123    0.2791]])

for b = 1:2:5
    bvals = ones(size(bvecs, 2), 1) * b;
    X = dti_design_matrix(bvecs, bvals);
    Q = [1.5, 0, 0; 0, 0.5, 0; 0, 0, 0.5];
    lower_diagonal = [Q(1); Q(5); Q(9); Q(2); Q(4); Q(6)]; % Dxx, Dyy, Dzz, Dxy, Dxz, Dyz
    
    signal = exp(-bvals .* squeeze(diag(bvecs' * Q * bvecs)));
    
    fit_to = log(signal);
    
    estimate = X\fit_to;
    
    npt.assert_equal(estimate-lower_diagonal)<10e-5));
    
    estQ = [estimate(1), estimate(4), estimate(5);...
        estimate(4), estimate(2), estimate(6);...
        estimate(5), estimate(6), estimate(3)];
    
    pred_sig = exp(-bvals .* squeeze(diag(bvecs' * estQ * bvecs)));
    assert(all(abs(pred_sig - signal)<10e-5));
end



