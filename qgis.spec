Name:		qgis
Version:	0.3.0
Release:	0
License:	GPL
Group:		Applications/Engineering
Autoreqprov:	on
Source0:	%{name}-%{version}.tar.gz
URL:		http://qgis.sourceforge.net/
Summary:	Quantum GIS (QGIS) is designed to be a Geographic Information System (GIS) built for Linux/Unix.
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define prefix /usr

%description
Quantum GIS (QGIS) is designed to be a Geographic Information System
(GIS) built for Linux/Unix. QGIS will offer support for vector and
raster formats. Currently QGIS supports shapefiles and
PostgreSQL/PostGIS layers.

Planned features include:

    - Read and edit shapefiles
    - Display georeferenced rasters (tiff, png, geotiff)
    - Plugins to dynamically add new functionality to the application
    - Support for database tables
    - Support for spatially enabled tables in PostgreSQL using PostGIS
    - Map output
    - Script engine
    - Metadata support

Authors:
- ---------- Carl Anderson Christoph Spoerri <spoerri at
  users.sourceforge.net> Denis Antipov <rawbytes at
  users.sourceforge.net> Gary E.Sherman <sherman at mrcc dot com> Jens
  Oberender <j.obi at troja.net> Marco Hugentobler <mhugent at
  users.sourceforge.net> Mark Coletti <mcoletti at
  users.sourceforge.net> Masaru Hoshi Radim Blazek <blazek at itc.it>
  Steve Halasz <stevehalasz at users.sourceforge.net>

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
./configure --prefix=%{_prefix}
%{__make}
strip src/qgis


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
