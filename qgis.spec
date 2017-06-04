# TODO: python and server subpackages
Summary:	Quantum GIS (QGIS) - a Geographic Information System (GIS)
Summary(pl.UTF-8):	Quantum GIS (QGIS) - system informacji geograficznych (GIS)
Name:		qgis
Version:	2.18.9
Release:	1
License:	GPL v2+
Group:		Applications/Engineering
Source0:	http://qgis.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	d55d4931651d1967876ba89aab8d2935
# 1st chunk of https://daniele.vigano.me/git/dani/copr-dani-qgis/raw/25b8f81ccabbfdb183d4850a66e884c183444f14/qgis_sip-ftbfs.patch
Patch0:		%{name}_sip-ftbfs.patch
URL:		http://qgis.org/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
#BuildRequires:	QtTest-devel
BuildRequires:	QtUiTools-devel
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
BuildRequires:	qjson-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake >= 4.8.0
BuildRequires:	qwt-devel >= 5.0.0
BuildConflicts:	qwt-devel >= 6.1.0
# ...or -DWITH_QWTPOLAR=OFF
BuildRequires:	sip-PyQt4-qscintilla2
BuildRequires:	spatialindex-devel
BuildRequires:	sqlite3-devel
Suggests:	gpsbabel
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

%package grass
Summary:	GRASS support for QGIS
Summary(pl.UTF-8):	Wsparcie GRASS dla QGIS-a
Group:		Applications/Engineering
Suggests:	grass

%description grass
GRASS plugin for QGIS required to interface with the GRASS system.

%prep
%setup -q
%patch0 -p1

%build
%cmake . \
	-DGRASS_INCLUDE_DIR7=%{_includedir}/grass72 \
	-DQGIS_MANUAL_SUBDIR=/share/man \
	-DENABLE_TESTS:BOOL=FALSE
# TODO: rpm/qgis.spec.template

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_datadir}/mime/packages}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p debian/q*.desktop $RPM_BUILD_ROOT%{_desktopdir}
install -p debian/q*.png $RPM_BUILD_ROOT%{_pixmapsdir}
install -p debian/qgis.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages

# %find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CONTRIBUTE.md ChangeLog Exception_to_GPL_for_Qt.txt NEWS README.md
%attr(755,root,root) %{_bindir}/qbrowser
%attr(755,root,root) %{_bindir}/qgis
%attr(755,root,root) %{_libdir}/libqgis*.so.*.*.*
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/grass
%exclude %{_libdir}/%{name}/plugins/libgrass*.so
%exclude %{_libdir}/libqgisgrass*.so.*.*.*
%exclude %{_libdir}/libqgispython.so.*.*.*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/grass
%exclude %{_datadir}/%{name}/python
%{_desktopdir}/q*.desktop
%{_pixmapsdir}/q*.png
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/q*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqgis*.so
%{_includedir}/%{name}

%files grass
%defattr(644,root,root,755)
%{_libdir}/%{name}/grass
%attr(755,root,root) %{_libdir}/%{name}/plugins/libgrass*.so
%attr(755,root,root) %{_libdir}/libqgisgrass*.so.*.*.*
%{_datadir}/%{name}/grass
