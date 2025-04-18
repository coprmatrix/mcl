Name: mcl
Version: 1.0_git20250316
Release: 0
Summary: C++ implementation of a fast hash map and hash set using robin hood hashing
URL: https://github.com/azahar-emu/mcl
License: MIT
BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake(fmt)

Source: %{name}-%{version}.tar.bz2

%package devel
Summary: %{summary}.

%description devel
%{summary}.

%description
%{summary}.


%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -pv `dirname %{buildroot}/%{_libdir}`
mv -Tv %{buildroot}/usr/lib %{buildroot}/%{_libdir}
mv -Tv %{buildroot}/%{_libdir}/lib%{name}.so{,.0}
ln -sTfv lib%{name}.so.0 %{buildroot}/%{_libdir}/lib%{name}.so

%files
%_libdir/lib%{name}.so.0

%files devel
%_includedir/%{name}
%_libdir/cmake/%{name}
%_libdir/lib%{name}.so
