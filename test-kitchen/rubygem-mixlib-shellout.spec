# Generated from mixlib-shellout-3.2.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-shellout

Name: rubygem-%{gem_name}
Version: 3.2.7
Release: 1%{?dist}
Summary: Run external commands on Unix or Windows
License: Apache-2.0
URL: https://github.com/chef/mixlib-shellout
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5
BuildArch: noarch

%description
Run external commands on Unix or Windows.


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


%changelog
* Mon Apr 03 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 3.2.7-1
- Initial package
