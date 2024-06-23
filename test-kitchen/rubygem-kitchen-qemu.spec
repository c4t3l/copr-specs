# Generated from kitchen-qemu-0.2.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name kitchen-qemu

Name: rubygem-%{gem_name}
Version: 0.2.11
Release: 1%{?dist}
Summary: Kitchen::Driver::Qemu - A QEMU Driver for Test Kitchen
License: GPL-3.0+
URL: https://github.com/esmil/kitchen-qemu/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
Kitchen::Driver::Qemu - A QEMU Driver for Test Kitchen.


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
* Sat Sep 10 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.2.11-1
- Initial package
