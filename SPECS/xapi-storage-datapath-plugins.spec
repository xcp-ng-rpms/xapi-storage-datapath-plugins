Name:           xapi-storage-datapath-plugins
Version:        0.2.1
Release:        2%{?dist}
Summary:        Storage datapath plugins for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/xapi-storage-datapath-plugins
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
Requires:       xapi-storage

%description
Storage datapath plugins for the xapi toolstack.

%prep
%autosetup -p1 -n xapi-storage-datapath-plugins-0.2.1

%build

%install
DESTDIR=%{buildroot} SCRIPTDIR=%{_libexecdir}/xapi-storage-script/ PYTHONDIR=%{python_sitelib}/xapi/storage/datapath make install

%files
%doc README.md LICENSE
%{_libexecdir}/xapi-storage-script/datapath/raw+file
%{_libexecdir}/xapi-storage-script/datapath/vhd+file
%{_libexecdir}/xapi-storage-script/datapath/loop+blkback/*
%{_libexecdir}/xapi-storage-script/datapath/tapdisk/*
%{_libexecdir}/xapi-storage-script/datapath/raw+block/*
%{python_sitelib}/xapi/storage/datapath/*.py*

%changelog
* Wed Sep 30 2015 Robert Breker <robert.breker@citrix.com> - 0.2.1-2
- Don't overwrite the upstream default datapath plugin for raw+file

* Tue Sep 15 2015 David Scott <dave.scott@citrix.com> - 0.2.1-1
- Update to 0.2.1

* Fri Sep 11 2015 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package

