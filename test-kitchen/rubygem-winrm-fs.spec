# Generated from winrm-fs-1.3.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name winrm-fs

Name: rubygem-%{gem_name}
Version: 1.3.5
Release: 1%{?dist}
Summary: WinRM File System
License: Apache-2.0
URL: http://github.com/WinRb/winrm-fs
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4.0
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(rspec) >= 3.0
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(rubocop) >= 0.68.0
# BuildRequires: rubygem(rubocop) < 0.69
BuildArch: noarch

%description
Ruby library for file system operations via Windows Remote Management.


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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/rwinrmcp
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sat Sep 10 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 1.3.5-1
- Initial package
