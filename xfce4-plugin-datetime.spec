%define		org_name	xfce4-datetime-plugin

Summary:	A date and time plugin for the Xfce panel
Name:		xfce4-plugin-datetime
Version:	0.6.1
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-datetime-plugin/0.6/%{org_name}-%{version}.tar.bz2
# Source0-md5:	e82f51ff0e75a63e5cbd139e43e094f9
Patch0:		%{name}-ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-datetime-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	xfce4-panel-devel
Requires:	xfce4-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An additional clock for the Xfce panel which also shows the date, with
adjustable font.

%prep
%setup -qn %{org_name}-%{version}
%patch0 -p1

# non existing macro
sed -i 's|BM_DEBUG_SUPPORT.*||' configure.in

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libdatetime.so
%{_datadir}/xfce4/panel-plugins/datetime.desktop

