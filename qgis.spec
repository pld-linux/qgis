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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gpsimporter
%attr(755,root,root) %{_bindir}/gridmaker
%attr(755,root,root) %{_bindir}/qgis
%attr(755,root,root) %{_libdir}/libqgis.so.*.*.*
%{_libdir}/%{name}
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qgis-config
%attr(755,root,root) %{_libdir}/libqgis.so
%{_libdir}/libqgis.la
%dir %{_includedir}/qgis
%{_includedir}/qgis/qgis.h
%{_includedir}/qgis/qgisapp.h
%{_includedir}/qgis/qgisappbase.ui.h
%{_includedir}/qgis/qgisappbase.uic.h
%{_includedir}/qgis/qgisiface.h
%{_includedir}/qgis/qgisinterface.h
%{_includedir}/qgis/qgisplugin.h
%{_includedir}/qgis/qgsabout.ui.h
%{_includedir}/qgis/qgsabout.uic.h
%{_includedir}/qgis/qgsattributetable.h
%{_includedir}/qgis/qgsattributetablebase.ui.h
%{_includedir}/qgis/qgsattributetablebase.uic.h
%{_includedir}/qgis/qgsattributetabledisplay.h
%{_includedir}/qgis/qgsconfig.h
%{_includedir}/qgis/qgscontcoldialog.h
%{_includedir}/qgis/qgscontcoldialogbase.uic.h
%{_includedir}/qgis/qgscontinuouscolrenderer.h
%{_includedir}/qgis/qgscoordinatetransform.h
%{_includedir}/qgis/qgscustomsymbol.h
%{_includedir}/qgis/qgsdatabaselayer.h
%{_includedir}/qgis/qgsdataprovider.h
%{_includedir}/qgis/qgsdatasource.h
%{_includedir}/qgis/qgsdbsourceselect.h
%{_includedir}/qgis/qgsdlgvectorlayerproperties.h
%{_includedir}/qgis/qgsdlgvectorlayerpropertiesbase.uic.h
%{_includedir}/qgis/qgsfeature.h
%{_includedir}/qgis/qgsfeatureattribute.h
%{_includedir}/qgis/qgsfield.h
%{_includedir}/qgis/qgsgraduatedmarenderer.h
%{_includedir}/qgis/qgsgraduatedsymrenderer.h
%{_includedir}/qgis/qgsgramadialog.h
%{_includedir}/qgis/qgsgramadialogbase.uic.h
%{_includedir}/qgis/qgsgramaextensionwidget.h
%{_includedir}/qgis/qgsgrasydialog.h
%{_includedir}/qgis/qgsgrasydialogbase.uic.h
%{_includedir}/qgis/qgsgrasyextensionwidget.h
%{_includedir}/qgis/qgshelpviewer.h
%{_includedir}/qgis/qgshelpviewerbase.ui.h
%{_includedir}/qgis/qgshelpviewerbase.uic.h
%{_includedir}/qgis/qgsidentifyresults.h
%{_includedir}/qgis/qgsidentifyresultsbase.uic.h
%{_includedir}/qgis/qgslegend.h
%{_includedir}/qgis/qgslegenditem.h
%{_includedir}/qgis/qgslegenditembase.uic.h
%{_includedir}/qgis/qgslinestyledialog.h
%{_includedir}/qgis/qgslinestyledialogbase.uic.h
%{_includedir}/qgis/qgslinesymbol.h
%{_includedir}/qgis/qgsmapcanvas.h
%{_includedir}/qgis/qgsmaplayer.h
%{_includedir}/qgis/qgsmaplayerinterface.h
%{_includedir}/qgis/qgsmapserverexport.h
%{_includedir}/qgis/qgsmapserverexportbase.ui.h
%{_includedir}/qgis/qgsmapserverexportbase.uic.h
%{_includedir}/qgis/qgsmarkerdialog.h
%{_includedir}/qgis/qgsmarkerdialogbase.uic.h
%{_includedir}/qgis/qgsmarkersymbol.h
%{_includedir}/qgis/qgsmessageviewer.ui.h
%{_includedir}/qgis/qgsmessageviewer.uic.h
%{_includedir}/qgis/qgsnewconnection.h
%{_includedir}/qgis/qgsoptionsbase.ui.h
%{_includedir}/qgis/qgsoptionsbase.uic.h
%{_includedir}/qgis/qgspatterndialog.h
%{_includedir}/qgis/qgspatterndialogbase.uic.h
%{_includedir}/qgis/qgspluginitem.h
%{_includedir}/qgis/qgspluginmanager.h
%{_includedir}/qgis/qgspluginmanagerbase.uic.h
%{_includedir}/qgis/qgspluginmetadata.h
%{_includedir}/qgis/qgspluginregistry.h
%{_includedir}/qgis/qgspoint.h
%{_includedir}/qgis/qgspolygonsymbol.h
%{_includedir}/qgis/qgsprojectio.h
%{_includedir}/qgis/qgsprojectproperties.h
%{_includedir}/qgis/qgsprojectpropertiesbase.ui.h
%{_includedir}/qgis/qgsprojectpropertiesbase.uic.h
%{_includedir}/qgis/qgsprovidermetadata.h
%{_includedir}/qgis/qgsproviderregistry.h
%{_includedir}/qgis/qgsrangerenderitem.h
%{_includedir}/qgis/qgsrasterlayer.h
%{_includedir}/qgis/qgsrasterlayerproperties.h
%{_includedir}/qgis/qgsrasterlayerpropertiesbase.ui.h
%{_includedir}/qgis/qgsrasterlayerpropertiesbase.uic.h
%{_includedir}/qgis/qgsrect.h
%{_includedir}/qgis/qgsrenderer.h
%{_includedir}/qgis/qgsrenderitem.h
%{_includedir}/qgis/qgsscalecalculator.h
%{_includedir}/qgis/qgssimadialog.h
%{_includedir}/qgis/qgssimadialogbase.uic.h
%{_includedir}/qgis/qgssimarenderer.h
%{_includedir}/qgis/qgssinglesymrenderer.h
%{_includedir}/qgis/qgssisydialog.h
%{_includedir}/qgis/qgssisydialogbase.uic.h
%{_includedir}/qgis/qgssymbol.h
%{_includedir}/qgis/qgssymbologyutils.h
%{_includedir}/qgis/qgsvectorlayer.h
%{_includedir}/qgis/qgsvectorlayerproperties.h
%{_includedir}/qgis/qgsvectorlayerpropertiesbase.uic.h
%{_includedir}/qgis/splashscreen.h
%{_aclocaldir}/qgis.m4

%package static
%defattr(644,root,root,755)
%{_libdir}/libqgis.a
