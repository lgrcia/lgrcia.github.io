---
title: "nuance"
date: 2023-01-01T00:00:00+00:00
draft: false
type: code & paper
short: "Efficient detection of planets transiting active stars"
code: "https://github.com/lgrcia/nuance"
paper: "https://arxiv.org/abs/2402.06835v1"
---

The detection of planetary transits in the light curves of active stars, featuring correlated noise in the form of stellar variability, remains a challenge. Depending on the noise characteristics, we show that the traditional technique that consists of detrending a light curve before searching for transits alters their signal-to-noise ratio, and hinders our capability to discover exoplanets transiting rapidly-rotating active stars. We present *nuance*, an algorithm to search for transits in light curves while simultaneously accounting for the presence of correlated noise, such as stellar variability and instrumental signals. We assess the performance of *nuance* on simulated light curves as well as on the TESS light curves of 438 rapidly-rotating M dwarfs. For each dataset, we compare our method to 5 commonly-used detrending techniques followed by a search with the Box-Least-Square algorithm. Overall, we demonstrate that *nuance* is the most performant method in 93% of cases, leading to both the highest number of true positives and the lowest number of false positive detections. Although simultaneously searching for transits while modeling correlated noise is expected to be computationally expensive, we make our algorithm tractable and availa ble as the JAX-powered Python package *nuance*, allowing its use on distributed environments and GPU devices. Finally, we explore the prospects offered by the *nuance* formalism, and its use to advance our knowledge of planetary systems around active stars, both using space-based surveys and sparse ground-based observations.

