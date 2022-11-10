---
title: "portal"
date:  2022-01-01T00:00:00+00:00
draft: false
short: A web-based interface for the SPECULOOS survey
type: code
paper: https://ui.adsabs.harvard.edu/abs/2020SPIE11445E..21S/abstract
---

The [SPECULOOS survey](https://www.speculoos.uliege.be) generates approx. 70TB of raw images per night, thanks to its 8 robotic telescopes located around the globe. Once these data transferred, its [automatic reduction pipeline](https://ui.adsabs.harvard.edu/abs/2020MNRAS.495.2446M/abstract) produces daily light curves that need to be inspected and analyzed by a large consortium. To ease this collaborative process, [Peter Pihlmann Pedersen](https://github.com/ppp-one) (University of Cambridge) and I developed a web-based interface, allowing our teams to visualize various data products, as well as reporting any signal of interest to the rest of the consortium (see features below).


{{< rawhtml >}}
<div style="text-align:center">
 <img src="/images/portal.png" width="100%"></img>
</div>
{{< /rawhtml >}}

The frontend of the web-based interface is built using [VueJS](https://vuejs.org), with a backend following the [LAMP model](https://en.wikipedia.org/wiki/LAMP_(software_bundle)). Visualizations are built using the [plotly](https://plotly.com) library.