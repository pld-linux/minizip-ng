Summary:	zip manipulation library written in C
Summary(pl.UTF-8):	Biblioteka operacji na plikach zip napisana w C
Name:		minizip-ng
Version:	4.0.10
Release:	1
License:	Zlib
Group:		Libraries
#Source0Download: https://github.com/zlib-ng/minizip-ng/releases
Source0:	https://github.com/zlib-ng/minizip-ng/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9b4de14db78016419598d0f292fde244
Patch0:		%{name}-cmake.patch
URL:		https://github.com/zlib-ng/minizip-ng
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 3.13
BuildRequires:	openssl-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
minizip-ng is a zip manipulation library written in C that is
supported on Windows, MacOS, and Linux.

%description -l pl.UTF-8
minizip-ng to napisana w C biblioteka do operacji na plikach zip,
ze wsparciem na systemach Windows, MacOS i Linux.

%package devel
Summary:	Header files for minizip-ng library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki minizip-ng
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	openssl-devel
Requires:	xz-devel
Requires:	zlib-devel
Requires:	zstd-devel

%description devel
Header files for minizip-ng library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki minizip-ng.

%package apidocs
Summary:	API documentation for minizip-ng library
Summary(pl.UTF-8):	Dokumentacja API biblioteki minizip-ng
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for minizip-ng library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki minizip-ng.

%prep
%setup -q
%patch -P0 -p1

%build
# disable compat and get minizip-ng names
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/minizip-ng \
	-DMZ_COMPAT=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_libdir}/libminizip-ng.so.*.*.*
%ghost %{_libdir}/libminizip-ng.so.4

%files devel
%defattr(644,root,root,755)
%{_libdir}/libminizip-ng.so
%{_includedir}/minizip-ng
%{_pkgconfigdir}/minizip-ng.pc
%{_libdir}/cmake/minizip-ng

%files apidocs
%defattr(644,root,root,755)
%doc doc/{zip,*.md}
