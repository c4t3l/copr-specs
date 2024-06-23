# Generated from license-acceptance-2.1.13.gem by gem2rpm -*- rpm-spec -*-
%global gem_name license-acceptance

Name: rubygem-%{gem_name}
Version: 2.1.13
Release: 1%{?dist}
Summary: Chef End User License Agreement Acceptance
License: Apache-2.0
URL: https://github.com/chef/license-acceptance/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4
BuildArch: noarch

%description
Chef End User License Agreement Acceptance for Ruby products.


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
%{gem_instdir}/config
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile

%changelog
* Sat Sep 10 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 2.1.13-1
- Initial package
