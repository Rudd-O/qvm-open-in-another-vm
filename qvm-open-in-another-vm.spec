%define debug_package %{nil}

%define mybuildnumber %{?build_number}%{?!build_number:1}

Name:           qvm-open-in-another-vm
Version:        0.0.2
Release:        %{mybuildnumber}%{?dist}
Summary:        An application registration to open links and other documents in separate qubes
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/Rudd-O/%{name}
Source0:        https://github.com/Rudd-O/%{name}/archive/{%version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
Requires:       qubes-core-agent
Requires:       coreutils
Requires:       desktop-file-utils

%description
This program lets your desktop environment associate URLs and file types so they open in other qubes.

%prep
%setup -q

%build
# variables must be kept in sync with install
make DESTDIR=$RPM_BUILD_ROOT DATADIR=%{_datatir}

%install
rm -rf $RPM_BUILD_ROOT
# variables must be kept in sync with build
for target in install ; do
    make $target DESTDIR=$RPM_BUILD_ROOT DATADIR=%{_datadir}
done

%post
update-desktop-database &> /dev/null || :
touch --no-create /usr/share/pixmaps &>/dev/null || :
gtk-update-icon-cache /usr/share/pixmaps &>/dev/null || :

%files
%attr(0644, root, root) %{_datadir}/applications/%{name}.desktop
%attr(0644, root, root) %{_datadir}/pixmaps/%{name}.svg
%doc README.md

%changelog
* Tue Feb 01 2022 Manuel Amador (Rudd-O) <rudd-o@rudd-o.com>
- First release.
