# Generated from unicode-display_width-2.4.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unicode-display_width

Name: rubygem-%{gem_name}
Version: 2.4.2
Release: 1%{?dist}
Summary: Determines the monospace display width of a string in Ruby
License: MIT
URL: https://github.com/janlelis/unicode-display_width
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4.0
# BuildRequires: rubygem(rspec) >= 3.4
# BuildRequires: rubygem(rspec) < 4
BuildArch: noarch

%description
[Unicode 15.0.0] Determines the monospace display width of a string using
EastAsianWidth.txt, Unicode general category, and other data.


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
# rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Mon Apr 03 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 2.4.2-1
- Initial package
