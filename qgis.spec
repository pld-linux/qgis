Summary:	Quantum GIS (QGIS) is designed to be a Geographic Information System (GIS) built for Linux/Unix.
Name:		qgis
Version:	0.3.0
Release:	0
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/qgis/%{name}-%{version}.tar.gz
# Source0-md5:	f1f12a5991a9bdf2389cc8892c7801cd
URL:		http://qgis.sourceforge.net/
BuildRequires: gdal-devel
BuildRequires: qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define prefix /usr

%description
Quantum GIS (QGIS) is designed to be a Geographic Information System
(GIS) built for Linux/Unix. QGIS will offer support for vector and
raster formats. Currently QGIS supports shapefiles and
PostgreSQL/PostGIS layers.

%prep
%setup -q

%build
%configure --with-qtdir=%{_prefix}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO
