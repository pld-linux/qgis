Summary:	Quantum GIS (QGIS) - a Geographic Information System (GIS) built for Linux/Unix
Summary(pl):	Quantum GIS (QGIS) - system informacji geograficznych (GIS) dla Linuksa/Uniksów
Name:		qgis
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/qgis/%{name}-%{version}.tar.gz
# Source0-md5:	f6ae20c4ae638f321bb3863783b6be3b
Patch0:		%{name}-paralelbuild.patch
URL:		http://qgis.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdal-devel
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRequires:	qt-linguist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quantum GIS (QGIS) is designed to be a Geographic Information System
(GIS) built for Linux/Unix. QGIS will offer support for vector and
raster formats. Currently QGIS supports shapefiles and
PostgreSQL/PostGIS layers.

%description -l pl
Quantum GIS (QGIS) jest projektowany by byæ systemem informacji
geograficznych (GIS - Geographic Information System) stworzonym dla
Linuksa/Uniksów. QGIS bêdzie oferowa³ obs³ugê formatów wektorowych i
rastrowych. Aktualnie QGIS obs³uguje pliki kszta³tów oraz warstwy
PostgreSQL/PostGIS.

%package devel
Summary:	Header files for QGIS
Summary(pl):	Pliki nag³ówkowe QGIS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for QGIS.

%description devel -l pl
Pliki nag³ówkowe QGIS.

%package static
Summary:	Static QGIS library
Summary(pl):	Statyczna biblioteka QGIS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static QGIS library.

%description static -l pl
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gridmaker
%attr(755,root,root) %{_bindir}/qgis
%attr(755,root,root) %{_libdir}/libqgis.so.*.*.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qgis-config
%attr(755,root,root) %{_libdir}/libqgis.so
%{_libdir}/libqgis.la
%{_includedir}/qgis
%{_aclocaldir}/qgis.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libqgis.a
