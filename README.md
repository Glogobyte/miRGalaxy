miRGalaxy: a Galaxy‑based framework for interactive analysis of microRNA and isomiR sequencing data 
=================================

:whale: Galaxy Docker repository for miRNA analysis (Galaxy flavour) - this is a base image containing NGS tools for:

  - QC
  - Pre-processing
  - Alignment
  - Identification - Quantification of miRNAs and IsomiRs
  - Differential Expression
  - Visualization

Usage
=====
At first you need to install docker. Please follow the instruction on https://docs.docker.com/installation/

After the successful installation, all what you need to do is:

``docker run -d -p 8080:80 glogobyte/mirgalaxy``

Docker images are "read-only", all your changes inside one session will be lost after restart. This mode is useful to present Galaxy to your colleagues or to run workshops with it. To install Tool Shed repositories or to save your data you need to export the calculated data to the host computer.

Fortunately, this is as easy as:

``docker run -d -p 8080:80 -v /home/user/galaxy_storage/:/export/ glogobyte/mirgalaxy``

With the additional ``-v /home/user/galaxy_storage/:/export/`` parameter, docker will mount the folder ``/home/user/galaxy_storage`` into the Container under ``/export/``. A ``startup.sh`` script, that is usually starting Apache, PostgreSQL and Galaxy, will recognize the export directory with one of the following outcomes:

  - In case of an empty ``/export/`` directory, it will move the [PostgreSQL](http://www.postgresql.org/) database, the Galaxy database directory, Shed Tools and Tool Dependencies and various config scripts to /export/ and symlink back to the original location.
  - In case of a non-empty ``/export/``, for example if you continue a previouse session within the same folder, nothing will be moved, but the symlinks will be created.

This enables you to have different export folders for different sessions - means real separation of your different projects.


By default, Galaxy instances launched with this image will have on-demand access to approximately 3TB of
reference genomes and indexes. These are the same reference data available on the main Galaxy server.
This is achieved by connecting to Galaxy's CernVM filesystem (CVMFS) at `data.galaxyproject.org` repository,
which is geographically distributed among numerous servers.
The CVMFS capability doesn't add to the size of the Docker image, but when running, CVMFS maintains
a cache to keep the most recently used data on the local disk.

*Note*: If you want to use on-demand the CVMFS reference genomes and indexes, you must launch Docker as `--privileged`


Users & Passwords
================

The Galaxy Admin User has the username ``admin`` and the password ``password``.
If you want to create new users, please make sure to use the ``/export/`` volume. Otherwise your user will be removed after your docker session is finished.


Requirements
============

- [docker](https://docs.docker.com/installation/)


Credits [[link]](https://github.com/bgruening/docker-galaxy-stable)
============
Many thanks to the Galaxy community!\
For more full description of the options of Galaxy docker:
- [Galaxy-docker](https://github.com/bgruening/docker-galaxy-stable)



Contacts
============
Ilias Glogovitis\
Researcher at University of Plovdiv\
PhD candidate at VU University Medical Center\
ilias@uni-plovdiv.bg


Licence (MIT)
=============

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
