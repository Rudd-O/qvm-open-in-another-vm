# Qubes: open URL / file in another qube

This is a very simple desktop file to let you associate certain URLs or file types so they will always launch in another VM.

This is based on https://github.com/Qubes-Community/Contents/blob/master/docs/common-tasks/opening-urls-in-vms.md#configuring-srcvm .

## How to use this program

You can associate files with this program, or you can associate URLs.  Here are details:

### How set URLs to open in a separate VM

Launch the app qube where you intend to use this.

Open the GNOME control center in the app qube (for reference, the command to launch it is `gnome-control-center`).  It may take a little while for that settings app window to show up.

Go to the section of the app named *Default applications*.

Select *Open in another Qube* as the *Web* default.

Presto — now clicking on URLs in other applications will launch a window asking you to select a VM to open the URL into.


## Installation instructions

First, install it (see below).

* Build the package by checking out the source and issuing `make rpm`.
* Copy the `noarch.rpm` file to your template qube.
* Install it in your template qube using your package manager (or `rpm -ivh <name of the package>`).

Power off the template qube, then power off any qubes based on that template.

You are ready to use it.
