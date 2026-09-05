**Yes, both Microsoft and Google are actively investing in photonics, but their efforts focus more on optical interconnects and specialized accelerators than on building general-purpose “photon computers” that fully replace electronic CPUs/GPUs.**

### Microsoft
Microsoft is the more advanced of the two in actual optical *computing* hardware:

- It has developed and publicly demonstrated an **Analog Optical Computer (AOC)**. The latest version (shown in 2025) uses micro-LEDs, lenses, and smartphone-camera sensors. It targets AI inference and combinatorial optimization problems and is claimed to be potentially ~100× faster or more energy-efficient than conventional digital hardware for certain workloads. Results were published in *Nature*. Microsoft Research plans new generations roughly every two years and envisions eventual use inside Azure data centers.
- It is also heavily developing **optical interconnects** (Project Mosaic / MOSAIC) that use inexpensive micro-LEDs for low-power, longer-reach links inside data centers. These are progressing toward commercialization with partners (e.g., MediaTek) targeted for late 2027.
- Additional research includes photonic Ising machines for optimization and adaptive photonic switching.

Microsoft is hiring for photonic AI architectures and interconnects and treats this as part of its Future AI Infrastructure effort. It is pursuing specialized optical accelerators + better optical networking rather than a complete general-purpose photonic replacement for electronics.

### Google
Google’s public work is more centered on **optical networking and interconnects** for its AI/TPU clusters:

- It pioneered and widely deploys **optical circuit switches (OCS)** (e.g., Apollo) in its data centers to reduce power and latency compared with traditional electronic switches.
- It is driving demand for high-speed optical modules (800G and beyond) and advanced optical architectures for large-scale TPU systems.
- Project Suncatcher explores space-based AI infrastructure that relies on free-space optical links between satellites.
- There is some photonic quantum research, but little evidence of a classical general-purpose photonic processor comparable to Microsoft’s AOC.

Google is a major force in scaling optical interconnects for AI infrastructure, but it has not publicly shown a full optical computer for general AI compute.

### Summary
| Company    | Optical Computing (processing with light) | Optical Interconnects / Networking | Near-term Goal                          |
|------------|-------------------------------------------|------------------------------------|-----------------------------------------|
| Microsoft | Yes – Analog Optical Computer (active prototypes) | Yes – micro-LED links (Mosaic), commercial path | Specialized AI/optimization accelerators + data-center optics |
| Google    | Limited public evidence of classical photonic processors | Very strong – OCS, high-speed modules, free-space optics | Massive AI cluster networking & scale   |

Both companies see photonics as essential for the energy and bandwidth walls of large-scale AI. Microsoft is further along in building actual optical computing hardware for specific workloads, while Google leads in deploying optical networking at hyperscale. Neither has announced plans for a fully general-purpose photonic computer that would replace conventional electronics across the board in the near future. Most near-term impact will come from hybrid systems (electronic compute + optical interconnects/accelerators).
