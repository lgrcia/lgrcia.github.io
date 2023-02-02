---
title: "nuance"
date: 2023-01-01T00:00:00+00:00
draft: false
type: code & paper
short: "Searching for transits in correlated noise"
code: "https://github.com/lgrcia/nuance"
paper: "https://github.com/lgrcia/paper-nuance/blob/main/latex/ms.pdf"
---

We present `nuance`, an algorithm to search for planetary transits in light curves featuring correlated noise, such as instrumental signals and stellar photometric variability. To deal with these nuisance signals, a common approach consists in cleaning a light curve from correlated noise before searching for transits. However, we show that this approach, based on the prior assumption that transits are not present, strongly degrades their signals, up to the point of no detection. As this degradation depends on the correlated noise characteristics, we explore the parameter space for which transits are altered, and quantify this effect on a wide variety of cases. We show that `nuance` outperforms the detection capabilities of commonly used transit search algorithms, especially for light curves featuring correlated noise with an amplitude three times greater than the searched transit depth. We perform our tests by injecting transits on synthetic light curves, and on known TESS candidates light curves to assess the performance of our algorithm on realistic multi-planetary systems datasets. Beyond its detection efficiency, we make `nuance` tractable, *TODO* times faster than current alternatives based on brute force detrending, and available as a well documented open-source Python package.

