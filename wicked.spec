Summary:	wicked - a lua library for dynamic widgets in awesome
Name:		wicked
Version:	20080914
Release:	0.1
License:	GPL v2
## git clone git://git.glacicle.com/awesome/wicked.git
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	6767c4570adf4993a388a1055af85227
Group:		X11/Window Managers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wicked is a library, written in lua, for easy creation and management
of dynamic awesome statusbar widgets, from the rc.lua configuration
file.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib
install -d $RPM_BUILD_ROOT%{_mandir}/man7
install wicked.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib
install wicked.7.gz $RPM_BUILD_ROOT%{_mandir}/man7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_mandir}/man7
%{_datadir}/awesome/lib/wicked.lua
%{_mandir}/man7/wicked.7*
