# Generated from chef-utils-17.10.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name chef-utils

Name: rubygem-%{gem_name}
Version: 17.10.0
Release: 1%{?dist}
Summary: Basic utility functions for Core Chef Infra development
License: Apache-2.0
URL: https://github.com/chef/chef/tree/main/chef-utils
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.6
BuildArch: noarch

%description
Basic utility functions for Core Chef Infra development.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/chef-utils.gemspec
%{gem_instdir}/spec

%changelog
* Sat Sep 10 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 17.10.0-1
- Initial package
