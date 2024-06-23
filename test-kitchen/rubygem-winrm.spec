# Generated from winrm-2.3.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name winrm

Name: rubygem-%{gem_name}
Version: 2.3.6
Release: 1%{?dist}
Summary: Ruby library for Windows Remote Management
License: Apache-2.0
URL: https://github.com/WinRb/WinRM
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.0
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(rb-readline)
# BuildRequires: rubygem(rexml)
# BuildRequires: rubygem(rspec) >= 3.2
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(rubocop) >= 0.51.0
# BuildRequires: rubygem(rubocop) < 0.52
BuildArch: noarch

%description
Ruby library for Windows Remote Management.


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
%{_bindir}/rwinrm
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sat Sep 10 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 2.3.6-1
- Initial package
