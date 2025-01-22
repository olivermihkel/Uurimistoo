import numpy as np


def density_disc(R, z, D=1e8, Rd=2.15, zh=0.4):
    """
    Return density of the stellar disc at Galactocentric distance R and vertical
    height z
    
    Input
    ----
        R  : Galactocentric distance [kpc]
        z  : vertical height wrt Galactic plane corresponding to z=0 [kpc]
        D  : normalisation constant [Msun/kpc3]
        Rd : scale-radius [kpc]
        zh : scale-length [kpc]
    """
    return D * np.exp(-R/Rd) * np.exp(-np.abs(z)/zh)


def mass_disc(R, D=1e8, Rd=2.15, zh=0.4):
    """
    Return stellar disc mass within a spherical cylinder of radius R
    and height 2*R. Note that owing to the planar configuration of the 
    stellar disc this is basically the mass within a sphere of radius R.
    
    Input
    -----
        R: Galactocentric distance [kpc]
    """
    from scipy import integrate
    # return
    return 2*np.pi*integrate.dblquad(density_disc, -R, R, 0, R, args=(D, Rd, zh))[0]
