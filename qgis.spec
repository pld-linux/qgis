Summary:	Quantum GIS (QGIS) - a Geographic Information System (GIS) built for Linux/Unix
Summary(pl):	Quantum GIS (QGIS) - system informacji geograficznych (GIS) dla Linuksa/uniksów
Name:		qgis
Version:	0.3.0
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/qgis/%{name}-%{version}.tar.gz
# Source0-md5:	f1f12a5991a9bdf2389cc8892c7801cd
URL:		http://qgis.sourceforge.net/
BuildRequires:	gdal-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quantum GIS (QGIS) is designed to be a Geographic Information System
(GIS) built for Linux/Unix. QGIS will offer support for vector and
raster formats. Currently QGIS supports shapefiles and
PostgreSQL/PostGIS layers.

%description -l pl
Quantum GIS (QGIS) jest projektowany by byæ systemem informacji
geograficznych (GIS - Geographic Information System) stworzonym dla
Linuksa/uniksów. QGIS bêdzie oferowa³ obs³ugê formatów wektorowych i
rastrowych. Aktualnie QGIS obs³uguje pliki kszta³tów oraz warstwy
PostgreSQL/PostGIS.

%prep
%setup -q

%build
%configure \
	--with-qtdir=%{_prefix}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
