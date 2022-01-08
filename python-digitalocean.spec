#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-digitalocean
Version  : 1.14.0
Release  : 20
URL      : https://github.com/koalalorenzo/python-digitalocean/archive/v1.14.0.tar.gz
Source0  : https://github.com/koalalorenzo/python-digitalocean/archive/v1.14.0.tar.gz
Summary  : digitalocean.com API to manage Droplets and Images
Group    : Development/Tools
License  : LGPL-3.0
Requires: python-digitalocean-license = %{version}-%{release}
Requires: python-digitalocean-python = %{version}-%{release}
Requires: python-digitalocean-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jsonpickle)
BuildRequires : pypi(requests)
BuildRequires : pypi(responses)

%description
<h1 align="center">python-digitalocean</h1>
<p align="center">Easy access to Digital Ocean APIs to deploy droplets, images and more.</p>

%package license
Summary: license components for the python-digitalocean package.
Group: Default

%description license
license components for the python-digitalocean package.


%package python
Summary: python components for the python-digitalocean package.
Group: Default
Requires: python-digitalocean-python3 = %{version}-%{release}

%description python
python components for the python-digitalocean package.


%package python3
Summary: python3 components for the python-digitalocean package.
Group: Default
Requires: python3-core
Provides: pypi(python_digitalocean)
Requires: pypi(jsonpickle)
Requires: pypi(requests)
Requires: pypi(responses)

%description python3
python3 components for the python-digitalocean package.


%prep
%setup -q -n python-digitalocean-1.14.0
cd %{_builddir}/python-digitalocean-1.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641654194
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-digitalocean
cp %{_builddir}/python-digitalocean-1.14.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-digitalocean/c09f9595f49b611cb4815dac18057910e5ff66b3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-digitalocean/c09f9595f49b611cb4815dac18057910e5ff66b3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
