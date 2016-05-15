Summary:	Quantum GIS (QGIS) - a Geographic Information System (GIS)
Summary(pl.UTF-8):	Quantum GIS (QGIS) - system informacji geograficznych (GIS)
Name:		qgis
Version:	2.14.2
Release:	0.1
License:	GPL v2+
Group:		Applications/Engineering
Source0:	http://qgis.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	be8427d171adb07f454e9f3eea349dea
#Patch0:		%{name}-paralelbuild.patch
URL:		http://qgis.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	bison >= 2.4
BuildRequires:	cmake >= 2.8.6
BuildRequires:	expat-devel >= 1.95
BuildRequires:	flex >= 2.5.6
BuildRequires:	gdal-devel >= 1.4.0
BuildRequires:	geos-devel >= 3.4.0
BuildRequires:	grass-devel >= 6.0.0
BuildRequires:	gsl-devel >= 1.8
BuildRequires:	libspatialite-devel
BuildRequires:	postgresql-devel >= 8.0.0
BuildRequires:	proj-devel >= 4.4.0
BuildRequires:	python-PyQt4-devel-tools >= 4.8.3
BuildRequires:	python-PyQt4-uic	 >= 4.8.3
BuildRequires:	python-PyQt4-qscintilla2
BuildRequires:	python-devel >= 2.7
BuildRequires:	python-sip-devel >= 4.12
BuildRequires:	qca-devel
BuildRequires:	qscintilla2-qt4-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	qwt-devel >= 5.0.0
BuildConflicts:	qwt-devel >= 6.1.0
# ...or -DWITH_QWTPOLAR=OFF
BuildRequires:	spatialindex-devel
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quantum GIS (QGIS) is designed to be a Geographic Information System
(GIS) built for Linux/Unix. QGIS will offer support for vector and
raster formats. Currently QGIS supports shapefiles and
PostgreSQL/PostGIS layers.

%description -l pl.UTF-8
Quantum GIS (QGIS) jest projektowany by być systemem informacji
geograficznych (GIS - Geographic Information System) stworzonym dla
Linuksa/Uniksów. QGIS będzie oferował obsługę formatów wektorowych i
rastrowych. Aktualnie QGIS obsługuje pliki kształtów oraz warstwy
PostgreSQL/PostGIS.

%package devel
Summary:	Header files for QGIS
Summary(pl.UTF-8):	Pliki nagłówkowe QGIS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for QGIS.

%description devel -l pl.UTF-8
Pliki nagłówkowe QGIS.

%package static
Summary:	Static QGIS library
Summary(pl.UTF-8):	Statyczna biblioteka QGIS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static QGIS library.

%description static -l pl.UTF-8
Statyczna biblioteka QGIS.

%prep
%setup -q
#%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--with-qtdir=%{_prefix}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}{,/designer}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gridmaker
%attr(755,root,root) %{_bindir}/qgis
%attr(755,root,root) %{_bindir}/qgis_help
%attr(755,root,root) %{_bindir}/spit
%attr(755,root,root) %{_libdir}/libqgis.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%dir %{_libdir}/%{name}/designer
%attr(755,root,root) %{_libdir}/%{name}/designer/*.so
%{_datadir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qgis-config
%attr(755,root,root) %{_libdir}/libqgis.so
%{_libdir}/libqgis.la
%{_includedir}/%{name}
%{_aclocaldir}/qgis.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libqgis.a
