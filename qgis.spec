Summary:	Quantum GIS (QGIS) - a Geographic Information System (GIS) built for Linux/Unix
Summary(pl.UTF-8):	Quantum GIS (QGIS) - system informacji geograficznych (GIS) dla Linuksa/Uniksów
Name:		qgis
Version:	0.7.0
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/qgis/%{name}-%{version}.tar.gz
# Source0-md5:	ffec37c0b4b2fff4bb689801b641eadb
Patch0:		%{name}-paralelbuild.patch
URL:		http://qgis.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdal-devel
BuildRequires:	geos-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRequires:	qt-linguist
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
%patch0 -p1

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
