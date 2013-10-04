
Name: alterator-postinstall
Version: 0.1
Release: alt1

Source:%name-%version.tar

Packager: Logvinov Sergey <serge.logvinov@gmail.com>

Summary: alterator module for postinstall script installer
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Requires: alterator >= 4.17-alt1
Requires: alterator-l10n >= 2.1-alt4

BuildPreReq: alterator >= 4.17-alt1


# Automatically added by buildreq on Thu Sep 05 2013
BuildRequires: alterator

%description
alterator module for postinstall script installer

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*

%changelog
* Thu Sep 05 2013 Logvinov Sergey <serge.logvinov@gmail.com> 0.1-alt1
- Initial release

