# Generated from kitchen-salt-0.7.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name kitchen-salt

Name: rubygem-%{gem_name}
Version: 0.7.2
Release: 1%{?dist}
Summary: Salt provisioner for test-kitchen
License: Apache-2.0
URL: https://github.com/saltstack/kitchen-salt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
Salt provisioner for test-kitchen so that you can test all the things.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Sun Sep 11 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.7.2-1
- Initial package
