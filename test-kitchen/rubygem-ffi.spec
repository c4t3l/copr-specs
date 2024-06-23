# Generated from ffi-1.15.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ffi

Name: rubygem-%{gem_name}
Version: 1.15.5
Release: 1%{?dist}
Summary: Ruby FFI
License: BSD-3-Clause
URL: https://github.com/ffi/ffi/wiki
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.3
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: make
BuildRequires: libffi-devel
# BuildRequires: rubygem(rake-compiler) >= 1.0
# BuildRequires: rubygem(rake-compiler) < 2
# BuildRequires: rubygem(rake-compiler-dock) >= 1.0
# BuildRequires: rubygem(rake-compiler-dock) < 2
# BuildRequires: rubygem(rspec) >= 2.14.1
# BuildRequires: rubygem(rspec) < 2.15

%description
Ruby FFI library.


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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/LICENSE.SPECS
%{gem_libdir}
%{gem_instdir}/rakelib
%{gem_instdir}/samples
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ffi.gemspec

%changelog
* Mon Apr 03 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 1.15.5-1
- Initial package
