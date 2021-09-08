%global debug_package %{nil}

Name: python-antsibull
Epoch: 100
Version: 0.44.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Ansible Build Scripts
License: GPL-3.0-only
URL: https://github.com/ansible-community/antsibull/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Tooling for building various things related to Ansible.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-antsibull
Summary: Ansible Build Scripts
Requires: make
Requires: python3
Requires: python3-aiocontextvars
Requires: python3-aiofiles
Requires: python3-aiohttp >= 3.0.0
Requires: python3-ansible-pygments
Requires: python3-antsibull-changelog >= 0.14.0
Requires: python3-asyncio-pool
Requires: python3-docutils
Requires: python3-importlib-metadata
Requires: python3-Jinja2
Requires: python3-packaging >= 20.0
Requires: python3-perky
Requires: python3-pydantic
Requires: python3-PyYAML
Requires: python3-rstcheck >= 3
Requires: python3-semantic_version
Requires: python3-sh
Requires: python3-Sphinx
Requires: python3-twiggy >= 0.5.0
Provides: python3-antsibull = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-antsibull
Tooling for building various things related to Ansible.

%files -n python%{python3_version_nodots}-antsibull
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-antsibull
Summary: Ansible Build Scripts
Requires: make
Requires: python3
Requires: python3-aiocontextvars
Requires: python3-aiofiles
Requires: python3-aiohttp >= 3.0.0
Requires: python3-ansible-pygments
Requires: python3-antsibull-changelog >= 0.14.0
Requires: python3-asyncio-pool
Requires: python3-docutils
Requires: python3-importlib-metadata
Requires: python3-Jinja2
Requires: python3-packaging >= 20.0
Requires: python3-perky
Requires: python3-pydantic
Requires: python3-PyYAML
Requires: python3-rstcheck >= 3
Requires: python3-semantic_version
Requires: python3-sh
Requires: python3-Sphinx
Requires: python3-twiggy >= 0.5.0
Provides: python3-antsibull = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull) = %{epoch}:%{version}-%{release}

%description -n python3-antsibull
Tooling for building various things related to Ansible.

%files -n python3-antsibull
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-antsibull
Summary: Ansible Build Scripts
Requires: make
Requires: python3
Requires: python3-aiofiles
Requires: python3-aiohttp >= 3.0.0
Requires: python3-ansible-pygments
Requires: python3-antsibull-changelog >= 0.14.0
Requires: python3-asyncio-pool
Requires: python3-docutils
Requires: python3-jinja2
Requires: python3-packaging >= 20.0
Requires: python3-perky
Requires: python3-pydantic
Requires: python3-pyyaml
Requires: python3-rstcheck >= 3
Requires: python3-semantic_version
Requires: python3-sh
Requires: python3-sphinx
Requires: python3-twiggy >= 0.5.0
Provides: python3-antsibull = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull) = %{epoch}:%{version}-%{release}

%description -n python3-antsibull
Tooling for building various things related to Ansible.

%files -n python3-antsibull
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
