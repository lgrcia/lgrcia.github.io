---
title: "prose"
date: 2022-03-01T00:00:00+00:00
draft: false
short: "Modular and transparent image processing pipelines"
type: code & paper
code: "https://github.com/lgrcia/prose"
paper: "https://ui.adsabs.harvard.edu/abs/2022MNRAS.509.4817G/abstract"
---

In Astronomy, a large number of observations lead to 2D images, often recorded in time. Either dealing with raw images or processed products, scientists must generally employ or trust [pipelines](https://en.wikipedia.org/wiki/Pipeline_(computing)): a set of processing units sequentially executed on each image before being combined into exploitable datasets: photometric or spectroscopic light curves, spatial profiles, transients detection… and so on. Given their complexity and size, pipelines can be challenging to understand, document and maintain. This is particularly true for pipelines dedicated to medium-size instruments, developed by scientists (not engineers) as monoliths, with hardcoded settings and poor documentation. In opposition, pipelines from larger-budget instruments benefit from proper engineering teams, putting effort into maintaining tools for the scientific community (as does [ESO](https://www.eso.org/public/) for example). 

For building cryptic monoliths, no one is to blame. Scientists often lack the time and expertise to build such softwares, and legitimately prefer spending energy on the methods they develop and the science they study. prose is a Python package allowing scientists to build robust, modular and transparent pipelines, focusing on what matters. By providing a set of pre-implemented (documented) blocks, one can easily assemble and test processing sequences, and only develop the blocks they need. Not only this approach yield reproducible tools, it allows for rapid iteration towards pipelines with optimal scientific products.

For more info check out the [documentation](https://lgrcia.github.io/prose-docs) and [paper](https://ui.adsabs.harvard.edu/abs/2022MNRAS.509.4817G/abstract)